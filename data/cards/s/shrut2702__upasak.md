# shrut2702/upasak

⭐ 21 · Python · MIT · 推送 2025-12-04 · [GitHub](https://github.com/shrut2702/upasak) · 个人维护

**面向隐私合规场景的 LLM 无代码/低代码微调框架**

基于 Hugging Face Transformers 与 Streamlit 的微调框架：通过 UI 选择模型（当前支持 Gemma-3 文本模型）、上传或从 HF Hub 导入数据集、自动识别 7 种数据集 schema、配置超参与 LoRA，完成全参或 LoRA 微调并生成推理脚本，可推送回 HF Hub。内置 PII 检测与脱敏（规则式默认，可选 GLiNER NER 混合模式，支持人工审核）。各内部模块（TokenizerWrapper、TrainingEngine、PIISanitizer）可脱离 UI 单独复用。限制：当前仅支持 Gemma-3 文本模型，LLaMA/Qwen 等为计划支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Streamlit 无代码界面覆盖选模型→脱敏→训练→导出全流程
- 自动识别 DAPT/ALPACA/CHATML 等 7 种数据集 schema
- 内置 PII 脱敏：规则式与 GLiNER NER 混合模式，支持人工审核
- 训练后自动生成适配的 inference.py 脚本，模块可编程复用

## 适用场景

- 在敏感或受监管数据上做内部 LLM 微调前先做 PII 脱敏
- 不写代码完成 Gemma-3 的指令微调或领域适配
- 将 PIISanitizer / TrainingEngine 等模块嵌入自有数据流水线

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: **Upasak** is a flexible, mindful to privacy, no-code/low-code framework for fine-tuning large language models, buil
> L17: * Developed on top of Hugging Face's Transformers library.

## 星数曲线

```mermaid
xychart-beta
    title "shrut2702/upasak 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fc71f32dbe70` · [字段定义](../../DATASET.md)*
