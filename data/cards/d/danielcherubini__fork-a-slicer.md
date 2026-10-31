# danielcherubini/fork-a-slicer

⭐ 30 · 推送 2026-05-13 · [GitHub](https://github.com/danielcherubini/fork-a-slicer) · 个人维护

**给 AI agent 使用的分步文档：指导 Fork OrcaSlicer 并接入 Bambu 打印机**

仅含文档与计划文件的仓库：通过 5 份顺序依赖的计划文档，指导用户 fork OrcaSlicer，并基于 FULU-Foundation 架构搭建进程隔离桥，在独立进程中加载 Bambu Lab 闭源网络插件，实现 ARM Linux、摄像头、云功能等打印机控制。使用方式是将计划逐份交给 AI agent 执行。仓库声明不分发 Bambu 闭源插件、证书或私钥，引用挪威 Åndsverkloven §41/§42 与欧盟 2009/24/EC 论证逆向工程实现互操作的法律依据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 份顺序依赖的计划文档（证书提取、桥基础设施、接入 OrcaSlicer、构建验证）
- 进程隔离桥：独立进程运行 Bambu 网络插件，JSON-RPC 通信
- 附挪威法与欧盟指令下的逆向工程互操作法律框架说明
- 仅含文档与计划文件，不分发 Bambu 闭源组件

## 适用场景

- 我想给 OrcaSlicer 的 fork 添加 Bambu Lab 打印机支持
- 让 AI agent 按计划逐步执行 OrcaSlicer 的桥接改造
- 了解逆向工程实现打印机互操作的法律依据与边界

## 场景标签

 · 领域:3D 打印/软件互操作

## 证据(README 行号)

> L3: > Documentation and step-by-step plans that walk you through forking OrcaSlicer and adding Bambu printer support — u
> L14: Then feed each plan to your AI agent in order. Example:
> L83: This repository contains documentation and plan files only. All code you produce by following these plans is your o

## 星数曲线

```mermaid
xychart-beta
    title "danielcherubini/fork-a-slicer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `30803bbf8ecd` · [字段定义](../../DATASET.md)*
