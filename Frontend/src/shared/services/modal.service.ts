import { inject, Injectable, Type } from "@angular/core";
import { DialogService } from "primeng/dynamicdialog";
import { ModalComponent } from "../components/modal/modal.component";


type ModalContext = {
  component: Type<any>;
  data?: any;
  header: string;
  width?: string;
  onClose?: (res: any) => void;
}

type DynamicModalContext = { key: string } & ModalContext;

@Injectable({
  providedIn: "root",
})
export default class ModalService {

  protected dialogService: DialogService = inject(DialogService);

  open({ onClose = () => {}, ...context }: ModalContext) {
    if(!context.component) return;


    this.dialogService.open(ModalComponent, {
      data: {
        component: context.component,
        componentProps: context.data,
      },
      header: context.header,
      width: this.isMobile()? "95%" : context.width || "85%",
      style: { maxHeight: "95vh" },
      duplicate: true,
    })?.onClose.subscribe((res: any) => onClose(res))
  }

  dynamicOpen(key: string, config: DynamicModalContext[], data?: any, onClose: (res: any) => void = () => {}) {
    config.map(({ key: contextKey, data: contextData, onClose: contextOnClose = () => {}, ...context}) => {
      if(contextKey === key) this.open({ ...context, data: { ...data, ...contextData }, onClose: (res) => {
        contextOnClose(res);
        onClose(res);
      }});
    });
  }

  protected isMobile() {
    return window.innerWidth < 1199;
  }

}
