import { Component, inject, OnInit, Type, ViewContainerRef } from '@angular/core';
import { DynamicDialogConfig } from 'primeng/dynamicdialog';

@Component({
  standalone: true,
  selector: 'app-dialog',
  template: '',
})
export class ModalComponent implements OnInit {

  component: Type<any>;
  data: any;

  dialogConfig: DynamicDialogConfig = inject(DynamicDialogConfig);
  viewRef: ViewContainerRef = inject(ViewContainerRef);

  ngOnInit() {
    this.getComponent();
    this.getDialogDataRef();
    this.loadComponent();
  }

  loadComponent() {
    const componentRef = this.viewRef.createComponent(this.component);
    Object.keys(this.data).forEach(prop => {
      componentRef.instance[prop] = this.data[prop];
    });
  }

  getDialogDataRef() {
    this.data = this.dialogConfig?.data?.componentProps || {};
    console.log("DIALOG PROPS", this.data);
  }

  getComponent() {
    this.component = this.dialogConfig?.data?.component;
  }

}
