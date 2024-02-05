/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";
import { browser } from "@web/core/browser/browser";

export class ApprovedController extends ListController{
    setup(){
        super.setup()
        this.orm = useService("orm");
        this.notification = useService('notification');
    }
    OnTestClick(){
        console.log("Test button run successfully!!!!!")
    }
    async approve_button_click(){
            const record_ids = await this.getSelectedResIds();
            if(record_ids <= 0)
            {
                 this.notification.add(
                _t("No device is Selected"),
                { type: 'danger' },
            )
            }
            else{
            await this.orm.call('device.assignment', 'button_click', [record_ids]).then(() => {
                this.notification.add(
                _t("Your Device Assignment is Approved"),
                { type: 'success' },
            )
            });
            browser.location.reload();
            }
            console.log(record_ids);
    }

}


registry.category('views').add('approved', {
   ...listView,
   Controller: ApprovedController,
   buttonTemplate: "device_management.activate.button",
});