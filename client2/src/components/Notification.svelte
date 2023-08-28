<script>
  import { Dropdown, DropdownItem, Indicator, Avatar } from "flowbite-svelte";
  import "iconify-icon";
</script>

<div
  id="bell"
  class="absolute bottom-16 right-4 w-10 h-10 text-gray-500 bg-gray-200 dark:text-gray-400 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-500 rounded-lg text-xl p-2 inline-flex justify-center items-center"
>
  <iconify-icon icon="mdi:bell-ring" />
  <Indicator
    color="red"
    border
    size="xl"
    placement="top-right"
    class="text-xs font-bold text-white">20</Indicator
  >
</div>
<Dropdown
  placement="left"
  triggeredBy="#bell"
  class="w-full max-w-sm rounded divide-y divide-gray-100 shadow dark:bg-gray-800 dark:divide-gray-700"
>
  <div slot="header" class="text-center py-2 font-bold">Notifications</div>
  <DropdownItem class="flex space-x-4">
    <Avatar
      src="/images/profile-picture-1.webp"
      dot={{ color: "bg-gray-300" }}
      rounded
    />
    <div class="pl-3 w-full">
      <div class="text-gray-500 text-sm mb-1.5 dark:text-gray-400">
        New message from <span
          class="font-semibold text-gray-900 dark:text-white">Jese Leos</span
        >: "Hey, what's up? All set for the presentation?"
      </div>
      <div class="text-xs text-primary-600 dark:text-primary-500">
        a few moments ago
      </div>
    </div>
  </DropdownItem>
  <a
    slot="footer"
    href="/"
    class="block py-2 -my-1 text-sm font-medium text-center text-gray-900 bg-gray-50 hover:bg-gray-100 dark:bg-gray-800 dark:hover:bg-gray-700 dark:text-white"
  >
    <div class="inline-flex items-center">
      <svg
        class="mr-2 w-4 h-4 text-gray-500 dark:text-gray-400"
        aria-hidden="true"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
        ><path d="M10 12a2 2 0 100-4 2 2 0 000 4z" /><path
          fill-rule="evenodd"
          d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z"
          clip-rule="evenodd"
        /></svg
      >
      View all
    </div>
  </a>
</Dropdown>
