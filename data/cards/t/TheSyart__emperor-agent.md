# TheSyart/emperor-agent

⭐ 202 · TypeScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/TheSyart/emperor-agent) · [官网](https://github.com/TheSyart/emperor-agent) · 个人维护 · 中文 README

**本地运行的个人桌面 Agent 工作台（对话/项目工作/规划/持续任务）**

面向个人长期使用的本地单用户 Electron 桌面 Agent。支持 Chat 普通对话与 Build 项目工作两类会话，Agent 可在权限预设（read-only/workspace-write/danger-full-access）约束下读写文件、运行 Shell、使用工具、Skills、Plugins 与 MCP。提供 Plan 先规划后执行、Goal 自动续跑、Scheduler 定时触发、长期与项目私有记忆、子代理、Token 遥测。多 Provider 模型配置，DeepSeek 有内置适配器，其余走 OpenAI/Anthropic 协议。当前公开安装包为未签名 macOS Preview（arm64/x64），Windows/Linux 暂不更新；本地优先但不等于完全离线，请求会发送到所配 Provider。会话、记忆、附件均保存在本机 ~/.emperor。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Chat/Build 双会话类型与三级权限预设，Shell 在 macOS/Linux 走系统沙箱
- Plan 规划模式与 Goal 自动续跑（默认上限 256 轮）、Scheduler 定时任务
- 支持 Skills/Plugins/MCP 导入、子代理委派、多级记忆体系
- 实验性电脑操作（内置浏览器/Chrome/macOS 应用）与本机语音听写

## 适用场景

- 日常问答与绑定本地项目让 Agent 持续推进长任务
- 先审阅方案再让 Agent 执行的项目工作流
- 按时间定时发起任务或在空闲时自动续跑目标
- 在权限沙箱内让 Agent 读写文件、运行命令

## 场景标签

`AI 助手` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L8: Emperor Agent 是一款面向个人长期使用的桌面 Agent。你可以用它处理日常问答，也可以绑定本地项目，让 Agent 在明确的权限范围内读取文件、运行工具并持续推进任务。
> L48: 设置页可以保存多个标准接口模型，管理 Provider、协议、凭证和能力；当前使用哪个模型在聊天输入框中选择，切换从下一次请求开始生效。Provider 为 `deepseek` 时使用内置的 DeepSeek 适配器，其他 Pr
> L226: - Emperor Agent 是本地单用户 Electron 应用，不提供多人服务端部署。

## 星数曲线

```mermaid
xychart-beta
    title "TheSyart/emperor-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 197 --> 203
    line [198, 200, 202]
```

2026-10-18 198 → 2026-10-22 202（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0bbdcebba866` · [字段定义](../../DATASET.md)*
