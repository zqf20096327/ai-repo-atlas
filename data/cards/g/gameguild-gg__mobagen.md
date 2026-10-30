# gameguild-gg/mobagen

⭐ 80 · C++ · Apache-2.0 · 推送 2026-10-08 · [GitHub](https://github.com/gameguild-gg/mobagen) · 组织维护

**模块化 C++ 游戏引擎教学工具：跨平台、WebAssembly 优先**

面向游戏编程概念教学的模块化游戏引擎。核心以 C++ 编写，采用面向数据设计（DOD）与 ECS 架构，含无栈协程任务、响应式信号、无锁窃取式调度器，渲染基于 WebGPU/Dawn，SDL3 作为应用宿主，支持 ImGui/RmlUi 界面层与无头测试构建。引擎核心尽量精简，功能通过渲染、物理、音频等可替换模块扩展，脚本支持 JS/TS/WASM。编辑器规划为 Web 优先，构建产物为引擎播放器加模块、插件与资源的组合。提供在线 Demo（多为待实现的空模板，含 Flocking AI 示例与 WebGPU 医学体渲染 DICOM 查看器）。目标平台覆盖 iOS/Android/Windows/Linux/macOS/Web，使用 CMake 与 CPM 构建。多数模块（3D、物理、声音、网络、脚本、场景等）在清单中标记为未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- C++ 核心 + DOD/ECS 架构，无栈协程与无锁调度器
- 模块可替换设计：渲染/物理/音频等通过胶水代码接入核心
- WebGPU/Dawn 渲染，SDL3 宿主，支持 WebAssembly 与无头测试构建
- 在线 Demo 中含 Flocking AI 示例与 DICOM 医学体渲染查看器

## 适用场景

- 学习游戏引擎的模块化架构与 DOD/ECS 设计
- 在浏览器中体验或扩展引擎 Demo
- 作为游戏开发概念的教学中心参与社区共建

## 场景标签

 · 领域:游戏开发/教育

## 证据(README 行号)

> L3: MoBaGEn - Module Based Game Engine - Educational tool to teach game programming concepts.
> L30: - Flocking demo for this AI class.
> L31: - DICOM Viewer — WebGPU-based medical volume rendering.

## 星数曲线

```mermaid
xychart-beta
    title "gameguild-gg/mobagen 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 78 --> 81
    line [79, 80, 80]
```

2026-10-18 79 → 2026-10-30 80（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `18fcd37f7dea` · [字段定义](../../DATASET.md)*
