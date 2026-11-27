# p-svacha/ProceduralTextGeneration

⭐ 13 · ASP.NET · 推送 2026-11-26 · [GitHub](https://github.com/p-svacha/ProceduralTextGeneration) · 个人维护

**Unity 程序化词名生成工具：用 Markov 链/CNN 生成虚构词汇**

一个 Unity 项目，包含多种程序化文本/词汇生成方法及配套数据集，全部为自制实现，不依赖外部库。含两个主生成器：Classic Generator 支持 Markov 链或 CNN 生成行星、国家、省份、矿物等特定类型词汇；Geographical Generator 根据出身地区与性别生成人物（姓、名、性别、家乡）。提供已构建的 exe，运行后选择生成器、属性与过滤器，点击 Generate 即产出结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Classic Generator 支持 Markov 链（可调 n-gram 长度）与 CNN（可调训练迭代与 skew factor）两种方法
- Geographical Generator 按出身与性别生成人物姓名与家乡
- 全部实现自制，不使用外部库
- 提供可运行的 Windows exe 构建

## 适用场景

- 为游戏地图批量生成省份、国家、行星等名称
- 为虚拟角色生成符合出身背景的人名与家乡
- 按属性与过滤器筛选生成结果的类型

## 场景标签

 · 领域:游戏开发/程序化内容生成

## 证据(README 行号)

> L2: This unity project contains different approaches and datasets to procedurally generate words of a certain type. All 
> L5: - A Classic Generator, which allows you to generate words of a certain type (planets, countries, provinces, minerals


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `c5c8ef9e490e` · [字段定义](../../DATASET.md)*
