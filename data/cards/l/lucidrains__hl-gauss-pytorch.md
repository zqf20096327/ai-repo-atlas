# lucidrains/hl-gauss-pytorch

⭐ 81 · Python · MIT · 推送 2026-09-02 · [GitHub](https://github.com/lucidrains/hl-gauss-pytorch) · 个人维护

**PyTorch 实现的高斯直方图损失（HL-Gauss）回归损失库**

将 Imani 等人提出的 Gaussian Histogram Loss 以 PyTorch 模块形式实现，把回归问题转化为直方图分类损失；提供 HLGaussLoss 损失模块与从 embedding 到 logits 的 HLGaussLayer 便捷封装，可通过 use_regression=True 回退到常规回归以做消融对比。面向深度学习与价值型强化学习研究者/开发者使用，依据为 DeepMind Stop Regressing 论文附录 A 的定义。以 pip 安装的 Python 库形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HLGaussLoss 损失模块，按 Stop Regressing 论文附录 A 定义
- HLGaussLayer 封装：从 embedding 直接预测到 logits
- use_regression=True 可回退常规回归，便于消融实验

## 适用场景

- 价值型 RL 中用分类损失替代回归损失训练价值函数
- 回归任务中尝试分布化直方图损失
- 对比 HL-Gauss 与常规回归的消融实验

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: The Gaussian Histogram Loss (HL-Gauss) proposed by Imani et al. with a few convenient wrappers, in Pytorch.
> L19: The `HLGaussLoss` module as defined in Appendix A. of the Stop Regressing paper

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/hl-gauss-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-25 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3b37216ad8df` · [字段定义](../../DATASET.md)*
