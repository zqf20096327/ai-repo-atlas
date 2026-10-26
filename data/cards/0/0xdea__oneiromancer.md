# 0xdea/oneiromancer

⭐ 146 · Rust · MIT · 推送 2026-10-25 · [GitHub](https://github.com/0xdea/oneiromancer) · [官网](https://ollama.com) · 个人维护

**逆向工程助手：本地 LLM 辅助分析 Hex-Rays 伪代码**

Rust 编写的逆向工程辅助工具，调用本地运行的、针对 Hex-Rays 伪代码微调的 LLM（aidapal，基于 mistral-7b-instruct）分析函数或代码片段，输出代码功能的高层描述、推荐函数名与变量重命名建议，并将改进后的伪代码保存到单独文件。通过 Ollama 加载模型，可配合伪代码提取器 haruspex 与常用 IDE 使用，也可作为库被其他 crate 调用。经 cargo 安装，在 macOS/Ubuntu/Windows 11 上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Hex-Rays 伪代码微调的 LLM aidapal（mistral-7b-instruct）
- 输出代码描述、推荐函数名与变量重命名建议
- 改进后的伪代码保存为 .out.c 文件
- 可作库调用：analyze_code / analyze_file

## 适用场景

- 分析反编译伪代码时获取功能描述与命名建议
- 批量改进函数伪代码的可读性
- 在 Rust 项目中嵌入伪代码分析能力

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: Oneiromancer is a reverse engineering assistant that uses a locally running LLM that has been fine-tuned for Hex-Ra
> L17: - Cross-platform support for the fine-tuned LLM aidapal based on
> L18:  `mistral-7b-instruct`.

## 星数曲线

```mermaid
xychart-beta
    title "0xdea/oneiromancer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 145 --> 147
    line [146, 146]
```

2026-10-18 146 → 2026-10-26 146（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b6a4f88943f9` · [字段定义](../../DATASET.md)*
