# hitSlop/dotpop

⭐ 10 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/hitSlop/dotpop) · [官网](https://dotpop.click) · 组织维护

**用 Svelte 加 AI 编码 agent 在 Mac 上构建并分享本地迷你应用**

macOS 桌面应用与 CLI 组成的迷你应用平台：每个应用打包为单个 .pop 文件（SQLite 格式），携带界面、已保存数据与导入文件，可直接分享给安装了 dotpop 的用户。用户以 Svelte 编写应用，通过 pop CLI（describe/call/apply/batch）让 AI 编码 agent 与用户共同操作同一文档，agent 编辑可撤销、支持版本合并。本地使用无需账号，同步与实时协作可选；iPhone 应用处于 TestFlight。需 Bun 构建，开窗需 Mac 应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- .pop 文件为单 SQLite 文件，界面、数据与导入文件一体携带
- agent 通过 pop CLI 与用户操作同一文档，支持撤销与编辑合并
- CLI 自带引擎，可在 macOS/Linux 渲染模板图像并导出 PNG/PDF
- 支持相机/麦克风采集与端上录音转录

## 适用场景

- 和 AI agent 对话式定制周计划、清单等个人小工具
- 把填好的文档或空白模板发给他人直接使用
- 在 Mac 与 iPhone 间同步个人文档并实时协作编辑

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L16: Make little apps for your Mac with Svelte & your AI coding agent: a planner that fits your week, a recipe card cove
> L72: The Pop Wins tutorial below defines `countOne`. Each app exposes its own actions through `describe`; `apply` and `b
> L88: - Local documents need no account or server. Choose **Sync across devices** when creating a pop to keep it in sync 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `957b694b3c05` · [字段定义](../../DATASET.md)*
