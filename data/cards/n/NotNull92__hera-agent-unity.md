# NotNull92/hera-agent-unity

⭐ 30 · C# · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/NotNull92/hera-agent-unity) · 个人维护 · 中文 README

**让 AI 编程 agent 直接操作与验证实时 Unity Editor 的 CLI**

由 Go 编写的 CLI 工具，配合 Unity 项目内安装的 Connector 包，使 Codex、Claude Code、Cursor、Copilot 等可执行 shell 命令的编码 agent 能检查实时 Editor 状态、读写 Scene 与 GameObject、修改组件序列化值、执行项目 C#、运行 EditMode/PlayMode 测试、进入 Play Mode、截图验证与合成输入事件，形成观察→修改→运行→验证→修复的闭环。为 AI 上下文设计紧凑输出（list --compact 约 93 tokens），支持自建 [HeraTool] 扩展与危险操作预审批。要求的 Unity 版本下限为 6000.6，需通过 npm/安装脚本/go install 安装 CLI 并在 Unity Package Manager 添加 Connector 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Editor 状态、Scene/GameObject/组件读写、测试、Play Mode、截图与输入合成的 CLI 命令集
- 针对 AI 上下文的低 token 输出（list --compact 约 93 tokens）
- 支持项目自定义 [HeraTool] 命令与危险操作审批令牌
- 跨 Unity 版本（6000.6+）的编译门禁与真实 Editor 回归证据

## 适用场景

- 让编码 agent 在 Unity 中自行编译、测试并验证修改结果
- 不用人工在 AI 与 Unity 间来回复制粘贴错误与描述
- 让 agent 搭建并验证 uGUI 界面与动画资源

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14:  Codex, Claude, Cursor, Copilot, AntiGravity, and other shell-capable agents can inspect your live Unity Editor, ch
> L46: Hera does not replace Unity and it does not replace the coding agent. It connects the two so the agent can work wit
> L159: The normal production path is a CLI. Any agent that can run shell commands can use it.

## 星数曲线

```mermaid
xychart-beta
    title "NotNull92/hera-agent-unity 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-31 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f7f2d05dd02f` · [字段定义](../../DATASET.md)*
