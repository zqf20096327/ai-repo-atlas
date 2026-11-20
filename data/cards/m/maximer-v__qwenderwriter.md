# maximer-v/qwenderwriter

⭐ 8 · Python · NOASSERTION · 推送 2026-10-31 · [GitHub](https://github.com/maximer-v/qwenderwriter) · 个人维护

**将信贷决策系统编译进 0.8B 模型的开源实现**

以单个 safetensors 文件交付的信贷决策系统实现：在 Qwen3.5-0.8B 权重旁编译入 XGBoost 评分卡、精确 TreeSHAP 归因表与信贷策略张量。输入 23 字段申请即返回一份 JSON，含决策、违约概率区间、Shapley 驱动因素、策略量、数据质量标记、反事实行为变更建议、SHA-256 回执与经确定性校验器核验的说明段落（核验失败则不附）。模型权重不参与打分，全部数值来自编译张量。构建流程为 15 个脚本，重训后可替换特征契约与策略适配自有组合。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 评分卡、TreeSHAP 与策略以定点张量编译进 safetensors，输出与 booster 逐行一致
- 确定性校验器决定说明段落是否附发，防止语言层改动分数字段
- SHA-256 回执支持审计者不运行语言层即可复现整个决策
- UCI 基准上评分卡 ROC-AUC 0.778，逐次/批量、CPU/GPU 判定字段一致

## 适用场景

- 在信贷申请流程中生成带可复现回执的拒批/批准决定
- 向被拒申请人给出最小行为变更的反事实建议
- 替换特征契约与策略后适配自有信贷组合的评分卡构建
- 研究把树模型与策略编译进小型语言模型的实现方式

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5:  A complete credit decision system, from scorecard to verified explanation, compiled inside one 0.8B language model.
> L14: One `from_pretrained` call loads a Qwen3.5-0.8B model whose safetensors file also carries a gradient-boosted scorec
> L16: request and get back one JSON document: the decision and the rule that controlled it, the probability of default an

## 星数曲线

```mermaid
xychart-beta
    title "maximer-v/qwenderwriter 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-08", "2026-11-20"]
    y-axis "stars" 6 --> 9
    line [7, 8, 8]
```

2026-11-02 7 → 2026-11-20 8（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `973830fead65` · [字段定义](../../DATASET.md)*
