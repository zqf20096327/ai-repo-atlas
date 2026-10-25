# theprototype-app/core

⭐ 35 · JavaScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/theprototype-app/core) · [官网](https://theprototype.app) · 组织维护

**浏览器端 P2P 协作 3D 原型编辑器，含可选 AI 助手**

纯浏览器运行的协作 3D 编辑器：搭建几何体或导入模型、节点图编排行为、Rapier 物理、WebXR 全 VR 编辑；通过 peerjs mesh 点对点同步对象、语音、光标与文件，无后端，可自托管或指向自有信令服务器。AI 为可选功能：场景助手按提示词创建/移动/连线对象，经 ComfyUI/TRELLIS 或 Meshy 做文本生成 3D，需用户自带端点与密钥。技术栈 Svelte 5 + three.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- peerjs mesh 点对点实时协作，对象/节点图/语音/文件全量同步
- WebXR 全功能 VR 编辑（非仅查看模式）
- 节点图行为编排 + Rapier 物理 + 网格编辑与地形雕刻
- 可选 AI：提示词构建场景、ComfyUI/TRELLIS/Meshy 文本生成 3D，自带端点与密钥

## 适用场景

- 和他人无账号实时协作搭建 3D 原型并在 VR 中漫游
- 用提示词让 AI 助手创建和连线场景对象
- 自托管整个应用并接入自有信令服务器

## 场景标签

 · 领域:3D 创作/协作工具

## 证据(README 行号)

> L19: A collaborative 3D editor that runs entirely in the browser. Drop in primitives or your
> L54: **AI, if you want it 🤖**
> L57: - Text-to-3D through ComfyUI/TRELLIS or Meshy, imported straight into the scene

## 星数曲线

```mermaid
xychart-beta
    title "theprototype-app/core 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-25 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f72466a8622f` · [字段定义](../../DATASET.md)*
