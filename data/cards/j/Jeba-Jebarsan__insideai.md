# Jeba-Jebarsan/insideai

⭐ 20 · TypeScript · MIT · 推送 2026-07-18 · [GitHub](https://github.com/Jeba-Jebarsan/insideai) · 个人维护

**本地运行真实 LLM 的 3D 前向传播可视化教学工具**

在本地 CPU/GPU 上运行小型因果语言模型（默认 Qwen2.5-0.5B-Instruct），通过 WebSocket 将 tokenization、嵌入、注意力矩阵、MLP 激活、logits 与采样决策逐事件流式推送到 Next.js/Three.js 前端，以交互 3D 场景实时呈现生成过程。后端用 PyTorch eager attention 加 forward hooks 提取真实张量，降维处（4864 神经元→128 组、896 维→3 个 PCA 轴）在 UI 中标注。面向学习者与可解释性关注者，需 Python 3.11+ 与 Node 20+ 双进程启动，支持 Chat/Raw 模式、温度/top-k/top-p 与固定种子。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 注意力图/激活/logits 均来自模型真实前向传播，降维在 UI 中标注
- 默认本地运行 Qwen2.5-0.5B-Instruct，可切换 GPT-2/Llama 系任意因果 LM
- prefill + KV-cache decode，逐 token 经 WebSocket 流式推送
- 支持温度/top-k/top-p/重复惩罚/固定种子等采样控制

## 适用场景

- 直观理解 transformer 从 token 到输出的完整计算流程
- 课堂或演示中展示注意力与神经元激活的真实数值
- 用固定种子做可复现的教学演示

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: **Watch a real AI model think.** InsideAI runs a genuine language model on
> L13: **Yes.** By default InsideAI runs **Qwen2.5-0.5B-Instruct** (494M parameters,
> L105: The backend loads the model with eager attention (`output_attentions=True`)

## 星数曲线

```mermaid
xychart-beta
    title "Jeba-Jebarsan/insideai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a016dede561b` · [字段定义](../../DATASET.md)*
