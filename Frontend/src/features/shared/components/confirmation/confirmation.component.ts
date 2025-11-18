import { CommonModule } from '@angular/common';
import { Component, inject, Input } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { DialogService, DynamicDialogRef } from 'primeng/dynamicdialog';
import { ButtonSeverity } from '../../services/toast.service';

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
