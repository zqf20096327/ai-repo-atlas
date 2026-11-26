# ComfyShop-ORG/ComfyShop

⭐ 4 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/ComfyShop-ORG/ComfyShop) · 组织维护 · 中文 README

**ComfyUI 团队的开源自托管工作流生成平台**

将调好的 ComfyUI 工作流导出为 API JSON 后发布成网页生成表单，团队成员可在网页提交图片/视频生成任务、跟踪排队与执行进度、按历史参数重跑并公开作品。支持自建 GPU 工作机（独立运行或作 ComfyUI 插件）、RunningHub 连接两种执行通道；界面含 5 种语言，提供 Skill 供 Codex/Claude Code 查询与提交任务。Docker 部署或 Node.js+pnpm+uv 本地开发，数据存 SQLite/PostgreSQL 与本地或 S3 兼容存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 导入 ComfyUI API JSON 并发布为网页生成表单，含版本与发布机制
- 每次执行保留工作流版本、实际参数与种子，可从历史载入重跑
- 工作机独立运行或作为 ComfyUI 插件接入，每账号可绑定多台
- 提供 Skill 供 Codex/Claude Code 查询工作流、提交任务与取回成品

## 适用场景

- 团队内部把调好的 ComfyUI 工作流共享给非技术同事使用
- 自托管环境下管理图片/视频生成任务的提交、排队与执行记录
- 多人协作场景下按历史参数复现或迭代生成结果

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L8: **RunningHub 的开源自托管替代方案，面向使用 ComfyUI 的团队。**
> L10: 把调好的 ComfyUI 工作流发布成同事可以直接使用的生成表单。在同一个网页提交图片或视频生成任务、跟踪每次执行、找到原始成品，再用已有参数发起下一轮。个人和团队空间均可使用本空间的 ComfyUI 工作机、RunningHub
> L23: 2. **从网页提交生成。** 选择工作流，填写提示词、参考素材和其他参数。ComfyUI 工作流使用自己的在线工作机，RunningHub 工作流使用自己在相应站点的连接，官方模型由平台分配工作机。提交后可以跟踪排队和执行进度。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `7bf8c0fa17cc` · [字段定义](../../DATASET.md)*
