# ThisTakou/Converter-Python-to-Rust

⭐ 37 · Rust · MIT · 推送 2026-10-03 · [GitHub](https://github.com/ThisTakou/Converter-Python-to-Rust) · 个人维护

**用 LLM 把 Python 项目自动迁移为 Rust 的桌面应用**

基于 Tauri 2.0 的桌面应用，面向需要将 Python 代码迁移到 Rust 的开发者：扫描项目、检测依赖并从 300+ 库映射中建议对应 crate，将代码与上下文发给 LLM 生成 Rust，用 cargo check 校验并对编译错误做最多 5 次迭代修正。支持 OpenAI/Anthropic/Ollama/llama.cpp/Groq/Azure 等多种提供方，提供配置档案、成本追踪、并行迁移、试运行与报告导出。README 声明生成结果非 100% 准确，需人工复查，大项目 API 费用可能较高。

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

- LLM 生成 Rust 代码并以 cargo check 做编译校验与最多 5 次迭代修正
- 300+ Python→Rust 库映射与依赖自动检测
- 多 LLM 提供方支持（OpenAI/Anthropic/Ollama/llama.cpp/Groq/Azure/自定义）
- Windows/macOS/Linux 提供预构建安装包

## 适用场景

- 把存量 Python 项目逐步迁移到 Rust
- 在本地 Ollama/llama.cpp 模型上离线或低成本迁移代码
- 导出迁移报告并接入 CI/CD webhook 通知

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: py2rs is a desktop application that uses Large Language Models to automatically migrate Python projects to Rust. It 
> L16: - **LLM-Powered Migration** - Uses AI to understand Python code and generate equivalent Rust

## 星数曲线

```mermaid
xychart-beta
    title "ThisTakou/Converter-Python-to-Rust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3dbcf967e41d` · [字段定义](../../DATASET.md)*
