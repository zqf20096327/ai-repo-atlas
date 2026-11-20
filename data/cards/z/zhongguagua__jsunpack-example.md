# zhongguagua/jsunpack-example

⭐ 10 · JavaScript · 推送 2026-04-21 · [GitHub](https://github.com/zhongguagua/jsunpack-example) · [官网](https://www.jsunpack.tech/) · 个人维护 · 中文 README

**展示 jsunpack 反编译 Three.js+Vue2 游戏包结果的示例仓库**

该仓库本身不是工具，而是 jsunpack 反编译结果的展示案例：对一个用 webpack 打包成单文件的 Three.js + Vue 2 塔防游戏，jsunpack 恢复出 43 个源文件（映射覆盖约 90.7%），仓库按目录结构陈列还原结果，并附质量评估表（核心逻辑保留 92%、命名恢复约 93%、加权总分约 88%）与已知缺陷清单（如缺少 import 语句、几何体误判、4 个辅助文件未还原）。提供在线演示与源仓库链接，无安装或运行说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 陈列 webpack 单文件包还原出的完整项目源码结构
- 附量化质量评估：文件映射覆盖 90.7%、加权总分约 88%
- 逐模块列出还原细节（EventBus、EnemyFactory、Game.js 等）与已知缺陷

## 适用场景

- 评估 jsunpack 对真实 webpack 打包项目的还原效果
- 参考反编译输出的目录组织与命名恢复质量
- 对照已知缺陷清单判断手动修复工作量

## 场景标签

 · 领域:开发工具/逆向工程示例

## 证据(README 行号)

> L3: This repository demonstrates the decompilation results of jsunpack on a **Three.js + Vue 2 tower defense game** webp
> L22: ## Decompilation Quality Assessment

## 星数曲线

```mermaid
xychart-beta
    title "zhongguagua/jsunpack-example 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `92a254828ce2` · [字段定义](../../DATASET.md)*
