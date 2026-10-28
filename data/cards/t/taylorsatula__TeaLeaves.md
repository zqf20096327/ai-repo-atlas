# taylorsatula/TeaLeaves

⭐ 45 · Python · 推送 2026-07-16 · [GitHub](https://github.com/taylorsatula/TeaLeaves) · 个人维护

**给开发者的提示词注意力可视化与机制可解释性流水线**

机制可解释性（MI）流水线：在提示中定义命名区域（JSON 配置，支持标记/正则/字符范围），钩取每层注意力并做 logit lens 投影，输出逐 token 热力图、区域烹饪曲线、逐层动画与多变体对比报告（含 delta 表与多种子稳定性分析）。引擎从 HuggingFace 任意 decoder-only 模型自动发现架构，要求 attn_implementation='eager'（flash attention 不生成注意力矩阵）。本地 pip 安装，分析引擎需 GPU 环境（8B 约需 21GB VRAM），验证家族含 Qwen/Llama 3/Mistral/Gemma/gpt-oss。与 TransformerLens 等库不同，它是端到端产出分析的流水线而非钩子库。

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

- 区域标注自动映射 token 位置，处理 BPE 边界与 chat template 伪影
- 逐层注意力捕获 + logit lens token 排名轨迹
- 四种渲染器：热力图、烹饪曲线、逐层动画、多样本聚合
- 自动 N 变体对比：delta 表、多种子稳定性、markdown 报告

## 适用场景

- 量化提示词修改对注意力分布的影响，而非肉眼比对输出
- 调优系统提示词，观察各区域在层间的阶段化分工
- 对小模型做结构化输出的机制可解释性分析

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L15: Mechanistic interpretability pipeline for prompts. Annotate regions in any prompt, run attention capture and logit 
> L17: Existing MI tools (TransformerLens, NNsight, pyvene) are libraries: they give you hooks and activation access to bu

## 星数曲线

```mermaid
xychart-beta
    title "taylorsatula/TeaLeaves 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ae85356f838d` · [字段定义](../../DATASET.md)*
