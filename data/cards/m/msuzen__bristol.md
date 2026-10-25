# msuzen/bristol

⭐ 33 · Jupyter Notebook · GPL-3.0 · 推送 2026-03-20 · [GitHub](https://github.com/msuzen/bristol) · 个人维护

**随机矩阵集成生成与深度学习复杂度度量库（已冻结）**

Python 包，生成 Circular Unitary/Orthogonal/Symplectic Ensemble 随机矩阵并提供谱密度、谱遍历性等分析工具；核心功能 cPSE 作为深度网络复杂度度量，可判别添加更多层的收益停止点，支持 PyTorch 预训练模型（如 vgg11）直接计算。通过 random stream chunking 保证串行与并行运行的精确可复现。README 声明包已冻结不活跃，仅接受 Issue 问答，后续开发转移至 leymosun；配套 arXiv 论文与复现 notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成 CUE/COE/CSE 圆集成随机矩阵，串行与并行均精确可复现
- cPSE 复杂度度量：数据、学习与架构无关的加层停止判据
- 支持直接读取 PyTorch 预训练模型计算复杂度
- 提供复现三篇 arXiv 论文结果的 notebook

## 适用场景

- 度量深度网络复杂度并决定是否继续加层
- 神经架构搜索中的架构复杂度比较
- 生成可复现的圆集成随机矩阵并做谱分析
- 复现谱遍历性相关论文实验

## 场景标签

 · 领域:机器学习理论/科研工具

## 证据(README 行号)

> L29: Parallel random matrix tools and random matrix theory deep learning applications.
> L41: * Cascading Periodic Spectral Ergodicity (cPSE) : This is a complexity measure and could also detect when to stop a

## 星数曲线

```mermaid
xychart-beta
    title "msuzen/bristol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `acb0bf6e1c1d` · [字段定义](../../DATASET.md)*
