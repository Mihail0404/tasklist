export type TaskType = {
  name: string;
  description: string;
  date: Date;
};

export type ApiTaskType = {
  id: number;
  name: string;
  description: string;
  ownerId: number;
  createdAt: Date;
  completedAt: Date | null;
};
