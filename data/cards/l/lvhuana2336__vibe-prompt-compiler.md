# lvhuana2336/vibe-prompt-compiler

⭐ 3 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/lvhuana2336/vibe-prompt-compiler) · 个人维护 · 中文 README

**为 AI 编程工具用户把自然语言想法编译成可执行开发提示词**

本地优先的 Vibe Coding 需求编译器：把一句话需求拆解为目标、上下文、功能范围、工程约束、执行步骤和验收标准，最多追问 3 个补充问题后重新编译。提供本地规则引擎，无模型密钥也可用；配置模型后获得语义理解与追问，支持 OpenAI、Claude、Gemini、DeepSeek 等接口，并可按 Codex、Claude Code、Cursor 等工具调整执行约定。提供 Web、Windows 桌面安装包与 Android PWA，历史与配置保存在本地设备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六维需求诊断评分与最多 3 个高价值追问
- 输出执行版、分步版、精简版、需求规格和验收清单
- 本地规则引擎无密钥离线可用，模型失败时保留本地结果
- Windows 安装包内置运行时，不要求另装 Node.js

## 适用场景

- 把模糊想法整理成 AI 编程工具可直接执行的任务提示词
- 为 Codex、Claude Code、Cursor 等工具适配执行约定
- 接入自有的 OpenAI 兼容中转接口做提示词编译
- 在无密钥/离线环境下使用本地编译功能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: 言构是一款本地优先的 **Vibe Coding 需求编译器**。它不会只把一句话润色得更专业，而是把自然语言想法拆解成目标、上下文、功能范围、工程约束、执行步骤和验收标准，生成 AI 编程工具可以直接执行的开发提示词。
> L13: 项目同时提供 Web、Windows 桌面版和 Android PWA。没有模型密钥时也能完整使用本地编译器；配置模型后，可以获得更深入的语义理解与追问。
> L38: |本地优先|无密钥可用，模型失败时自动保留本地编译结果|

## 星数曲线

```mermaid
xychart-beta
    title "lvhuana2336/vibe-prompt-compiler 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-18 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `838fa3ca8f37` · [字段定义](../../DATASET.md)*
