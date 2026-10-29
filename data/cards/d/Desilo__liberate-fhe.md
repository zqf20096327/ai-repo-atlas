# Desilo/liberate-fhe

⭐ 147 · Python · BSD-3-Clause-Clear · 推送 2025-11-04 · [GitHub](https://github.com/Desilo/liberate-fhe) · [官网](https://docs.desilo.ai/) · 组织维护

**已弃用的全同态加密库：纯 Python+CUDA 多 GPU 加速**

Desilo 开源的全同态加密（FHE）库，基于纯 Python 与 CUDA 实现，支持 RNS-CKKS 方案、原生 Python 接口、多 GPU 加速与默认设置，以及多方 FHE。面向非密码学背景开发者，设计上追求少依赖、易修改、易与既有软件（尤其是 AI 相关）集成。通过 git clone 源码配合 poetry 或 pip 安装。注意：该库已声明不再维护，由后继库 DESILO FHE library（含 bootstrap 功能）替代。BSD 3-Clause Clear 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | BSD-3-Clause-Clear |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Python 与 CUDA 实现，原生支持多 GPU 操作
- 支持 RNS-CKKS 方案与多方 FHE（Multiparty FHE）
- 面向非密码学者设计，依赖少、易集成
- README 声明已弃用，由 DESILO FHE library 替代

## 适用场景

- 开发隐私保护的机器学习/数据科学应用
- 在密文上执行计算的多 GPU 加速场景
- 非密码学背景开发者快速上手 FHE 原型

## 场景标签

 · 领域:密码学/隐私计算

## 证据(README 行号)

> L17: Liberate.FHE is a pure Python and CUDA implementation of FHE. So, Liberate.FHE supports multi-GPU operations native
> L26: - Make the resulting library easily integrated with the pre-existing software, especially Artificial Intelligence (
> L13: Liberate.FHE is an open-source Fully Homomorphic Encryption (FHE) library for bridging the gap between theory and p

## 星数曲线

```mermaid
xychart-beta
    title "Desilo/liberate-fhe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 146 --> 148
    line [147, 147]
```

2026-10-18 147 → 2026-10-29 147（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `ef1b6b22d021` · [字段定义](../../DATASET.md)*
