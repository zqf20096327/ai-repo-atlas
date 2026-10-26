# 2389-research/dippin-lang

⭐ 33 · Go · 推送 2026-10-23 · [GitHub](https://github.com/2389-research/dippin-lang) · [官网](https://2389.ai/research/products/dippin-lang/) · 组织维护

**编写 AI pipeline 工作流的 DSL 语言与命令行工具链**

Dippin 是一种领域特定语言，用一等语法表达 AI 流水线中的提示词、shell 脚本、模型配置与分支逻辑，替代 Graphviz DOT 作为编写格式（DOT 仍作为可视化导出目标）。工具链提供验证/静态检查（DIP001–DIP165 诊断码）、模拟执行、成本估算、DOT 迁移、LSP 服务器，以及将工作流打包为内容寻址 .dipx 制品的命令。需 Go 1.21+ 以 go install 安装，agent 节点支持 anthropic/openai/gemini provider 与多种模型字段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一等语法表达 prompt、shell 脚本、模型配置与条件分支
- 诊断码体系（错误 DIP001–DIP010、警告 DIP101–DIP165）带位置与修复建议
- dippin migrate 将现有 DOT 流水线转为 Dippin 并校验结构等价
- deterministic .dipx 内容寻址打包，SHA-256 完整性校验
- 提供 LSP 服务器与 JSON 格式输出（面向 LLM 工具与 CI）

## 适用场景

- 以文本语言编写和校验多节点 AI agent 流水线
- 把存量 Graphviz DOT 流水线迁移为新格式并保持可视化导出
- 在 CI 中用 fmt --check 与 lint 检查流水线文件
- 模拟执行与成本估算，预估按模型/provider 的开销

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: A language and toolchain for authoring AI pipeline workflows.
> L5: Dippin is a domain-specific language that replaces Graphviz DOT as the authoring format for AI pipeline workflows. I

## 星数曲线

```mermaid
xychart-beta
    title "2389-research/dippin-lang 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `200dd681b8e1` · [字段定义](../../DATASET.md)*
