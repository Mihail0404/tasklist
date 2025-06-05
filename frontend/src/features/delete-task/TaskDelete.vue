<script setup lang="ts">
import * as Model from "./model";

defineProps<{
  id: number;
}>();

function deleteTask(id: number) {
  Model.deleteTask(id);
}
</script>

<template>
  <button class="delete" @click="deleteTask(id)">Удалить</button>
</template>
