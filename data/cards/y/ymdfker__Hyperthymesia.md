# ymdfker/Hyperthymesia

⭐ 3 · Python · 推送 2026-11-24 · [GitHub](https://github.com/ymdfker/Hyperthymesia) · 个人维护 · 中文 README

**给 AI agent 的跨会话长期记忆工具（MCP+钩子）**

通过 MCP 服务与钩子接入 Claude Code、Codex、WorkBuddy、Qoder、DeepSeek Harness 等 agent 宿主：每轮结束记录原话、回复与代码改动，积压约 28000 token 后由后台用宿主自身模型额度分两步整理进本机 `~/.hyperthymesia/`，下一轮注入相关记忆，个人记忆跨项目共享、项目记忆按目录隔离。凭据文件不读取、发送前遮盖密钥，非完全离线处理。提供 install/doctor/context/write/import/uninstall 等命令，脚本安装无需 Python。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP+钩子接入多种 agent 宿主，跨会话保留事实、决定与代码约定
- 后台用宿主自身最便宜的通过准入检查的模型整理，自动选型与用量日志
- 记忆存于本机目录，代码改动走独立影子仓库不改 git 历史
- import 命令可导入接入前的历史会话

## 适用场景

- 让编码 agent 新开会话时记得我的项目约定和此前的决定
- 把最近 7 天的历史对话补录进记忆库
- 在多个项目间共享个人偏好、项目内隔离各自约定

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: 给 AI agent 用的长期记忆。接入后，你在 Claude Code、Codex、WorkBuddy、Qoder、DeepSeek Harness 里说过的事实、做过的决定、
> L286: 每轮开始，钩子把相关记忆注入给 agent（记忆多时只注入目录，agent 通过 MCP 工具按需读取）；每轮结束，记下你的原话、
> L290: **后台整理分两步**：先把一批对话（默认积压约 28000 token 触发，单批上限约 40000 token，约 20 轮）分成最多 3 段逐轮抽取，材料按轮编号，模型只给出处编号，原文由程序复制；没抽到任何内容的轮次会单


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `646fe5b0c393` · [字段定义](../../DATASET.md)*
