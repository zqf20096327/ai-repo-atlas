# lxsolutions/studio-foundation

⭐ 30 · Python · NOASSERTION · 推送 2026-09-14 · [GitHub](https://github.com/lxsolutions/studio-foundation) · [官网](https://lxsolutions.github.io/studio-foundation/) · 组织维护

**面向 AI agent 的确定性游戏资产工具链与验证基座**

源码可获取（PolyForm Perimeter）的 AI-native 游戏开发工具包：核心组件 bforge 通过 138 个白名单化类型化操作驱动无头 Blender 守护进程生成 glTF/GLB 资产，输出字节级可复现，并有质量门（CIELAB ΔE、三角面预算、风格一致性）拒绝不达标导出。资产以引擎中立格式输出至 Godot/Babylon.js/three.js，Godot 为标准化运行时；另维护 Godot 4.7.1 WebGPU 浏览器后端的补丁系列，并提供冻结的 brief-to-asset 公开基准与 forge-live 网页演示。面向用 AI agent 构建游戏的小团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- bforge：138 个白名单化确定性操作驱动无头 Blender 守护进程，字节级可复现输出
- 质量门测量材质感知色差（CIELAB ΔE）、texel 密度、三角面预算并拒绝低质导出
- 资产以 glTF/GLB 引擎中立输出，进入 Godot/Babylon.js/three.js
- 维护 Godot 4.7.1 Forward+ 的 WebGPU 浏览器后端补丁系列（33 个校验和锁定补丁）

## 适用场景

- 让 AI agent 以确定性流水线生成可验证的 3D 游戏资产
- 在 CI 中对 agent 生成的资产做质量门与字节级复现校验
- 在浏览器中运行 Godot Forward+ 渲染的游戏（WebGPU 后端）

## 场景标签

 · 领域:游戏开发/3D 资产管线

## 证据(README 行号)

> L3: **An AI-native, source-available game-dev toolkit: the deterministic asset
> L11: - **bforge** — a deterministic headless-Blender asset forge for AI agents:

## 星数曲线

```mermaid
xychart-beta
    title "lxsolutions/studio-foundation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3e5d9d75ebfa` · [字段定义](../../DATASET.md)*
