# JuliusBrussee/cavegemma

⭐ 119 · Python · 推送 2026-07-09 · [GitHub](https://github.com/JuliusBrussee/cavegemma) · [官网](https://huggingface.co/JBrussee/gemma-4-31B-caveman) · 个人维护

**把“穴居人式”极简输出风格微调进 Gemma 4 31B 权重的 LoRA 模型**

对 google/gemma-4-31B-it 做 QLoRA 微调（rank 16，全部线性层），使模型无需系统提示或技能文件即以短句风格回答。193 对留出集上输出 token 减少 27%，语义相似度 0.91-0.98，代码围栏 96-100% 字节级保留。训练数据 1750 条，由 claude -p 与 codex exec 按 SKILL.md 规则合成，单卡 96GB Blackwell 约 50 分钟、花费 4-5 美元。发布 bf16 合并版（62.5GB）与 LoRA 适配器（534MB）两种权重，仓库含完整复现流程与评测脚本；README 自述压缩率未达金标准、review 类样本不足、多模态路径未验证等限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 193 对留出集：输出 token 减少 27%，语义相似度 0.91-0.98
- 代码围栏 96-100% 字节级保留
- 提供 bf16 合并版（62.5GB）与 LoRA 适配器（534MB）两种权重
- 完整复现流程：数据合成、训练、评测均含脚本，断点可续

## 适用场景

- 在无法控制系统提示的宿主/Agent 框架中获得极简输出风格
- 降低推理输出 token 成本与响应延迟
- 复现低成本（约 5 美元、50 分钟单卡）风格迁移微调流程

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L17: Gemma 4 31B, fine-tuned until it speaks caveman natively. No skill file. No system prompt. No `/caveman` toggle. Yo
> L98: |`JBrussee/gemma-4-31B-caveman`|bf16 merged|62.5 GB|Full Gemma 4 31B, caveman baked in. Drop-in.|

## 星数曲线

```mermaid
xychart-beta
    title "JuliusBrussee/cavegemma 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 118 --> 120
    line [119, 119]
```

2026-10-18 119 → 2026-10-24 119（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `6b762adf80df` · [字段定义](../../DATASET.md)*
