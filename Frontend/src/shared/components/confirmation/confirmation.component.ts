import { CommonModule } from '@angular/common';
import { Component, inject, Input } from '@angular/core';
import { ButtonModule, ButtonSeverity } from 'primeng/button';
import { DialogService, DynamicDialogRef } from 'primeng/dynamicdialog';

@Component({
  selector: 'app-confirmation',
  standalone: true,
  providers: [DialogService],
  imports: [ CommonModule, ButtonModule],
  templateUrl: './confirmation.component.html',
})
export class ConfirmationComponent {

  @Input() message: string;
  @Input() severity: ButtonSeverity = "primary";

  dialogRef: DynamicDialogRef = inject(DynamicDialogRef);

  confirm() {
    this.dialogRef.close({ status: "OK" });
  }

  cancel() {
    this.dialogRef?.close();
  }

}
