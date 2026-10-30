# Jamessfks/simpleatom

⭐ 17 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Jamessfks/simpleatom) · [官网](simpleatom.app) · 个人维护

**在浏览器中运行 MACE 机器学习势的原子模拟网页界面**

SimpleAtom 是 MACE（Message Passing Atomic Cluster Expansion）机器学习原子间势的 Web 前端：用户上传或绘制分子/晶体结构（.xyz/.cif/.poscar/.pdb、SMILES 转 3D、Ketcher 绘图），在浏览器中完成单点能、几何优化与分子动力学计算，附带 3D 查看器、轨迹动画与图表。v2.x 强调可复现性（模型检查点 SHA-256、MD 种子记录）与大声失败原则：不支持的计算（如 phonon、电子性质）直接报错而非静默返回。提供在线 Demo 与本地部署路径，面向化学/材料科研用户。

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

- 浏览器内运行 MACE-MP-0/MACE-OFF 的能量、力、应力与 MD 计算
- 每次计算附带可复现清单：检查点 SHA-256、依赖版本、MD 种子
- 结构输入支持文件上传、SMILES 转 3D 与 Ketcher 2D/3D 绘图
- 不支持的计算（phonon、电子密度相关性质）显式报错

## 适用场景

- 不装命令行工具在浏览器里跑机器学习势模拟
- 用 3D 查看器测键长、键角、二面角并导出结果
- 通过 MACE Link 分享含完整结果的计算链接

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: **Run DFT-accuracy atomistic simulations entirely in your browser.**
> L133: SimpleAtom is a wrapper around MACE. A wrapper's main risk
> L178: MACE is an interatomic potential. It produces energies, forces and stress, and has **no

## 星数曲线

```mermaid
xychart-beta
    title "Jamessfks/simpleatom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `41322b58a7a0` · [字段定义](../../DATASET.md)*
