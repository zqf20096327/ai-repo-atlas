# FerroxLabs/fuigo

⭐ 21 · Rust · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/FerroxLabs/fuigo) · [官网](https://www.npmjs.com/package/fuigo) · 组织维护

**开源编码 agent：任意模型、沙箱化、可脚本化可嵌入**

Rust 编写的命令行编码 agent，单一引擎提供三种使用界面：全屏终端 UI、无界面的 headless 模式（供脚本/CI 管道输出文本或 JSON）以及 ACP（JSON-RPC over stdio/WebSocket）服务模式供编辑器或自有应用调用。模型接入支持 OpenAI/Anthropic API key、ChatGPT/Grok 订阅登录、OpenAI 兼容网关与 Ollama 等本地服务器。内置权限审批、Landlock/Seatbelt 内核沙箱（默认关闭）、工作区记忆与 MCP/子代理/插件扩展。Apache-2.0，由 Ferrox Labs 内部开发并公开源码，不接受外部 PR。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单引擎三界面：终端 UI、headless -p 模式、ACP JSON-RPC 服务
- 任意模型路由：OpenAI/Anthropic key、ChatGPT/Grok 订阅、兼容网关、Ollama 本地服务器
- Landlock/Seatbelt 内核沙箱与逐项权限审批，默认询问后行动
- 工作区本地记忆默认开启，含来源标注与新鲜度检查

## 适用场景

- 在终端里让 AI 读写代码、跑测试并修复问题
- CI 中无人值守运行编码 agent（--yolo + JSON 输出）
- 通过 ACP 协议把编码 agent 嵌入编辑器或自己的产品

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: It isn't tied to one model company. Bring an OpenAI or Anthropic key, sign in with your ChatGPT subscription, or ru
> L45: - **One engine, three surfaces.** The same runtime behind the full-screen terminal UI, the headless `-p` command fo

## 星数曲线

```mermaid
xychart-beta
    title "FerroxLabs/fuigo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `76af7ec10155` · [字段定义](../../DATASET.md)*
