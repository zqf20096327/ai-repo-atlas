# zblasingame/Rex-solver

⭐ 14 · Python · MIT · 推送 2026-08-02 · [GitHub](https://github.com/zblasingame/Rex-solver) · [官网](https://rex-solver.github.io) · 个人维护

**扩散模型的可逆指数 Runge-Kutta 求解器参考实现**

ICML 2026 Oral 论文的官方实现：Rex 通过对显式（随机）Runge–Kutta 格式施加 Lawson 指数变换并套用 McCallum–Foster 可逆耦合，构造出在有限精度算术下代数可逆的求解器，支持概率流 ODE 与逆时间 SDE 两种设定，可作为扩散模型采样、反演、编辑与插值中标准求解器的替换。提供 11 种 Butcher 表（4 种支持自适应步长）与遗留固定步长 API（含 Euler–Maruyama、ShARK SDE 格式），附 CelebA-HQ、COCO、InstructPix2Pix、FRLL 实验脚本与 clean-FID 评测工具；数据集需自行下载，Stable Diffusion 实验需要 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 有限精度下代数可逆（前向+后向恢复原状态，至浮点误差）
- 继承底层 RK 格式的收敛阶，支持 ODE 与 SDE 两种设定
- 11 种 Butcher 表，其中 4 种支持自适应步长（dopri5/tsit5 等）
- 包含论文全部实验脚本与 clean-FID、编辑指标评测工具

## 适用场景

- 在扩散模型采样、反演、编辑与插值中替换标准求解器
- 复现论文的生成、编辑、插值与消融实验
- 研究可逆数值格式在扩散模型中的应用

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L15: Rex (**R**eversible **Ex**ponential) is a family of algebraically reversible
> L26: - is a drop-in replacement for standard solvers used for sampling, inversion,

## 星数曲线

```mermaid
xychart-beta
    title "zblasingame/Rex-solver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `5856ba9577af` · [字段定义](../../DATASET.md)*
