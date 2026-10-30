# ArnauMiro/pyLowOrder

⭐ 36 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/ArnauMiro/pyLowOrder) · [官网](https://arnaumiro.github.io/pyLowOrder/) · 组织维护

**面向 CFD/流体力学的并行降阶模型与深度学习代理建模库**

pyLOM 是一个 Python 编写的降阶建模（ROM）库，面向流体动力学与空气动力学应用。提供大规模并行实现的经典算法：本征正交分解（POD）、动态模态分解（DMD）、谱 POD（SPOD），以及变分自编码器等用于模型降阶与代理建模的深度学习架构；所有模块支持 GPU。由多所机构团队维护（作者列表含 UPC 等十余名研究者），研究受欧盟 NextSim 与西班牙科研项目资助。README 以引用论文为主，安装说明指向 wiki，仓库内可见测试套件与 DOI 徽章。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 并行实现的 POD/DMD/SPOD 经典降阶算法
- 变分自编码器等深度学习降阶与代理建模架构
- 所有模块 GPU 启用
- 配套十余篇期刊/会议论文描述实现与应用

## 适用场景

- 对 CFD 仿真数据做降阶分解与模态分析
- 构建流场/空气动力学问题的深度学习代理模型
- HPC 环境下大规模 SVD 与降阶计算

## 场景标签

 · 领域:科学计算/流体力学

## 证据(README 行号)

> L10: pyLOM is a high-performance-computing enabled tool for massively parallel reduced order modelling. This tool includ
> L23: Miró, A., Eiximeno, B., Gasparino, L., Kutz, N., Rodriguez, I., & Lehmkuhl, O. 2026. Toward a GPU-enabled billionai

## 星数曲线

```mermaid
xychart-beta
    title "ArnauMiro/pyLowOrder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-30 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6d5273901e5f` · [字段定义](../../DATASET.md)*
