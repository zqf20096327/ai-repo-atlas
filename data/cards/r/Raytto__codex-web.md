# Raytto/codex-web

⭐ 10 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Raytto/codex-web) · 个人维护 · 中文 README

**自托管的 Codex CLI 网页工作台：语音派活、远程执行、周期任务**

围绕 Codex CLI 构建的社区独立自托管 Web 工作台（与 OpenAI 无隶属关系），在浏览器中提供会话管理、文件上传下载、任务队列与执行记录持久化。语音输入经转写后交给 Agent，支持远程电脑派工（需 Remote Worker）、周期任务定时运行、任务中断续跑、文档问答，可按任务切换 Codex、Gemini/Antigravity 或显式配置的宿主 Claude Code。基础部署为 Linux + Docker，多会话并行并有用户/执行器级并发限制，默认不挂载 Docker socket。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音输入自动转写并委派给 Agent，支持连续通话与打断播报（需另配转写服务）
- 周期任务按天/周/间隔自动运行，任务可跨服务重启持久续跑
- 多执行器：同一工作台按任务选择 Codex、Gemini/Antigravity 或宿主 Claude Code
- 租户隔离与权限分离，Web 进程与执行进程使用不同 Unix 身份

## 适用场景

- 在手机或远程浏览器里给自己电脑上的 Codex 派任务并取回结果
- 让周期任务定时巡检、整理资料、生成报告
- 上传文档做问答并分享生成的报告

## 场景标签

`编码 Agent` `文档问答` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: 基于 Codex CLI 的自托管 AI 工作台：**语音交代需求，远程电脑执行，周期任务自动跑。**
> L29: - **多种引擎**：在同一个工作台中，按任务选择 Codex、Gemini / Antigravity，或显式配置的宿主 Claude Code。
> L156:     app --> tenant["隔离租户 → Codex CLI"]


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `9023a31ef231` · [字段定义](../../DATASET.md)*
