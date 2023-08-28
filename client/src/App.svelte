<script>
  import { Router, Route } from "svelte-navigator";
  import { DarkMode } from "flowbite-svelte";

  import SideBar from "@/components/SideBar.svelte";
  import Notification from "@/components/Notification.svelte";

  import Team from "@/pages/Team.svelte";
  import MoneyShare from "@/pages/MoneyShare.svelte";
  import Balance from "@/pages/Balance.svelte";
  import Settings from "@/pages/Settings.svelte";
  import Faq from "@/pages/FAQ.svelte";

  let btnClass =
    "text-gray-500 dark:text-gray-400 bg-gray-200 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-500 rounded-lg text-xl p-2";
</script>

<main>
  <Router>
    <div class="grid grid-cols-7 gap-2">
      <SideBar class="w-full" />
      <div class="col-span-6">
        <Route path="team" primary={true}>
          <Team />
        </Route>
        <Route path="money-share">
          <MoneyShare />
        </Route>
        <Route path="balance">
          <Balance />
        </Route>
        <Route path="settings">
          <Settings />
        </Route>
        <Route path="faq">
          <Faq />
        </Route>
      </div>
    </div>
    <!-- Dark mode -->
    <div class="absolute bottom-4 right-4 ...">
      <DarkMode size="lg" {btnClass} />
    </div>
    <!-- Notifications -->
    <Notification />
  </Router>
</main>
