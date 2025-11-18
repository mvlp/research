import { inject, Injectable } from "@angular/core";
import { MessageService, ToastMessageOptions } from "primeng/api";
import { Message } from "primeng/message";

export type ToastSeverity = "info" | "success" | "error" | "warn" | "secondary";
export type ButtonSeverity = "success" | "info"  | "danger" | "help" | "primary" | "secondary" | "contrast";

export type Toast = ToastMessageOptions & {
  severity: ToastSeverity;
}

@Injectable({
  providedIn: "root",
})
export default class ToastService {

  messageService: MessageService = inject(MessageService);
  key: string = "main-toast";

  add(message: Toast) {

    const asd = new Message()


    this.messageService.add({ key: this.key, ...message });
  }

  addAll(messages: Toast[]) {
    this.messageService.addAll(messages.map(message => ({ key: this.key, ...message })));
  }

  clear() {
    this.messageService.clear();
  }

}
