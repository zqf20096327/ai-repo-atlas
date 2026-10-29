# THU-WingTecher/LSPRAG

⭐ 43 · TypeScript · Apache-2.0 · 推送 2026-05-14 · [GitHub](https://github.com/THU-WingTecher/LSPRAG) · 组织维护

**基于 LSP 与 LLM 的多语言单元测试生成 VS Code 扩展**

面向开发者的 VS Code 扩展，结合 Language Server Protocol 语义代码分析与 LLM，在编辑器内实时生成单元测试。支持 Java（JUnit 4/5）、Python（pytest）与 Go（Go testing）三种语言，均标注 Production Ready。通过右键菜单对指定函数生成测试，提供 accept/reject 审阅流程，日志与生成的测试文件保存到工作区目录。LLM 供应商可在 DeepSeek、OpenAI、Ollama（本地）间配置，最多支持 3 轮细化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LSP 语义分析结合 LLM 生成单元测试
- 支持 Java/Python/Go 三种语言及对应测试框架
- 生成结果带 accept/reject 审阅，日志保存至工作区
- 可配置 DeepSeek/OpenAI/Ollama（本地）三种 LLM 供应商

## 适用场景

- 编码时在 VS Code 内为函数快速生成单元测试
- 为 Java/Python/Go 项目补充覆盖边界情况的测试用例
- 使用本地 Ollama 模型离线生成测试

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L26: LSPRAG (Language Server Protocol-based AI Generation) is a cutting-edge VS Code extension that leverages Language S
> L116: |Language|Status|Framework|Features|

## 星数曲线

```mermaid
xychart-beta
    title "THU-WingTecher/LSPRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `79f7d500205f` · [字段定义](../../DATASET.md)*
