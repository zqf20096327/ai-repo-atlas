# lucidrains/simple-hierarchical-transformer

⭐ 230 · Python · MIT · 推送 2026-09-23 · [GitHub](https://github.com/lucidrains/simple-hierarchical-transformer) · 个人维护

**在 GPT 中引入多层级预测编码的 Transformer 实验库**

lucidrains 的研究实验项目：在自回归 Transformer 中诱导多个分层预测编码模型，各层级基于下一因果 token 块的摘要进行下一潜变量预测，最细层级保留 next token 交叉熵。潜变量目标与块摘要均做 stop-gradient，层级可自定义维度（越上层维度越大），不指定层级参数时退化为常规自回归 Transformer。以 PyTorch 库形式经 pip 提供。作者自述这是简单想法的实验，可能不成立，若失败会保留负结果与仓库供后续研究者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多个层级并行的分层预测编码，均服务于下一 token 预测
- 内置 Teoh et al. 式 next latent prediction（MSE 与 cosine 相似度插值、rollout 动态降权）
- 各层级可自定义模型维度与摘要器（任意 nn.Module）
- 不指定层级/窗口参数时退化为常规全注意力自回归 Transformer

## 适用场景

- 研究分层预测编码在语言建模中的效果
- 实验局部注意力+分层 token 替代全注意力基线
- 基于代码探索不同压缩层级下的模型容量配置

## 场景标签

 · 领域:深度学习/语言模型研究

## 证据(README 行号)

> L3: Experiments around a simple idea for inducing multiple hierarchical predictive coding models within a GPT. It is so 
> L21: Three hierarchies, all servicing predicting the next token
> L32: Next latent prediction, following the scheme proposed by

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/simple-hierarchical-transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 229 --> 232
    line [231, 230]
```

2026-10-18 231 → 2026-10-22 230（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a1dc2d1a2114` · [字段定义](../../DATASET.md)*
