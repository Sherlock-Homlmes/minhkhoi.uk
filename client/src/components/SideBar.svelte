<script>
  import {
    Sidebar,
    SidebarWrapper,
    SidebarBrand,
    SidebarItem,
    SidebarGroup,
  } from "flowbite-svelte";
  import "iconify-icon";

  let site = {
    name: "Kpay Wallet",
    href: "/",
    img: "/Logo.png",
  };
  let imgClass = "h-16";
</script>

<Sidebar class="h-screen shadow-lg">
  <SidebarWrapper>
    <SidebarGroup>
      <SidebarBrand class="font-mono" {site} {imgClass} />
      <a href="/team">
        <SidebarItem label="Team">
          <svelte:fragment slot="icon">
            <iconify-icon icon="mdi:account-group" />
          </svelte:fragment>
        </SidebarItem>
      </a>
      <a href="/money-share">
        <SidebarItem label="Money share">
          <svelte:fragment slot="icon">
            <iconify-icon icon="mdi:account-cash" />
          </svelte:fragment>
        </SidebarItem>
      </a>
      <a href="/balance">
        <SidebarItem label="Balance">
          <svelte:fragment slot="icon">
            <iconify-icon icon="mdi:wallet" />
          </svelte:fragment>
        </SidebarItem>
      </a>
    </SidebarGroup>
    <SidebarGroup border="true">
      <a href="/settings">
        <SidebarItem label="Settings">
          <svelte:fragment slot="icon">
            <iconify-icon icon="mdi:cog" />
          </svelte:fragment>
        </SidebarItem>
      </a>
      <SidebarItem label="Sign Out">
        <svelte:fragment slot="icon">
          <iconify-icon icon="mdi:arrow-collapse-left" />
        </svelte:fragment>
      </SidebarItem>
    </SidebarGroup>
  </SidebarWrapper>
</Sidebar>

<div class="flex pt-16 overflow-hidden bg-gray-50 dark:bg-gray-900">
  <div
    id="main-content"
    class="relative w-full h-full overflow-y-auto bg-gray-50 lg:ml-64 dark:bg-gray-900 min-h-screen"
  >
    <slot />
  </div>
</div>
