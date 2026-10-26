# aixplain/koder

⭐ 34 · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/aixplain/koder) · [官网](https://koder.aixplain.com) · 组织维护

**桌面与终端 AI 编程代理，带权限检查与可审查改动**

aixplain 公司开发的 AI 编程代理，提供桌面应用（含 Koder 编程、Design 设计、Omni 个人助手三种模式）与终端 CLI。用自然语言描述任务后，代理读取代码、逐行可审查地编辑、运行测试，命令与文件修改前按权限模式（Ask first/Auto/Full access）征求批准，.env 等密钥文件在任何模式下读取前都会询问。模型可接 aixplain 托管目录、已有的 Claude/ChatGPT/Cursor 订阅（通过各厂商自己的 CLI）、API key 接入的兼容端点，或经 Ollama/内置引擎跑本地模型。另含安全扫描 Scan（输出 SARIF）与 17 种语言的界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三级权限模式与密钥文件读取强制审批
- 会话内全部改动汇总为一个可审查 diff
- Scan 安全扫描：按严重度列问题、追踪攻击路径、输出 SARIF 供 CI 使用
- 本地模型经 Ollama 或内置引擎运行，按机器内存与显卡推荐模型

## 适用场景

- 用自然语言让代理找 bug、加功能、写测试并审查每步改动
- 在 CI 中跑 koder scan 做安全扫描并按严重度失败
- 复用已付费的 Claude/ChatGPT/Cursor 订阅驱动代理
- 在本地跑模型进行离线编程辅助

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: Koder is an AI coding agent and assistant from aixplain for macOS, Windows and Linux. Use it in the desktop app or t
> L26: Koder is an AI coding agent: a model connected to your project through tools it can use, permissions it has to foll

## 星数曲线

```mermaid
xychart-beta
    title "aixplain/koder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `57baf9b91e2a` · [字段定义](../../DATASET.md)*
