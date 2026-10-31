# raghavagps/hemopi2

⭐ 18 · Python · GPL-3.0 · 推送 2026-07-13 · [GitHub](https://github.com/raghavagps/hemopi2) · [官网](http://webs.iiitd.edu.in/raghava/hemopi2/) · 组织维护

**预测多肽溶血活性（分类/回归）的生物信息学工具**

面向计算生物学研究者，HemoPI2 提供肽段溶血活性的鉴定（分类）与量化（回归）两种方法：分类可选 RF、蛋白质语言模型 ESM2-t6 及其与 MERCI 基序模块的混合模型；回归基于随机森林回归器预测 HC50/EC50 浓度值。功能包括肽段预测、蛋白质序列中溶血区域扫描、指定位置突变体设计与全突变体设计及活性预测。输入支持 FASTA 与简单格式，输出 CSV。以 pip 包与 Python3 独立版提供，独立版需从服务器下载并解压压缩的模型文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分类模型含 RF、ESM2-t6 及 ESM2-t6+MERCI 混合（默认）
- 回归模块基于随机森林预测 HC50/EC50
- 支持蛋白质扫描、定点突变设计与全突变体设计的活性预测
- MERCI 基序扫描定位溶血基序

## 适用场景

- 预测候选肽段是否具有溶血活性及溶血浓度 HC50
- 在长蛋白质序列中扫描潜在溶血区域
- 设计突变肽并预测其溶血活性变化

## 场景标签

 · 领域:计算生物学/生物信息学

## 证据(README 行号)

> L4: HemoPI2 is developed for identification (Classification) as well as quantification (regression) methods for predicti

## 星数曲线

```mermaid
xychart-beta
    title "raghavagps/hemopi2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `aaf99c60b970` · [字段定义](../../DATASET.md)*
