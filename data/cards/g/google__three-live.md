# google/three-live

⭐ 516 · TypeScript · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/google/three-live) · [官网](https://google.github.io/three-live/) · 组织维护

**把 AI 生成的 Three.js 编译为多平台原生 3D/XR 的运行时**

端上 JIT 编译器与运行时：将标准 Three.js 代码在沙箱 Rust VM 中编译，原生渲染到 Android（Filament/Jetpack XR）、iOS/visionOS（RealityKit）及 WebGL2/WebXR。提供 three-live-cli 无头渲染接触表、.glb/.usdz 转换、MCP stdio 服务器与 agent gym 供 AI 编码代理使用；Web 组件支持接入任意 LLM 后端进行场景编辑、图像转场景、语音选择与 AI 纹理生成，编辑先沙箱编译并自动修复后才热替换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端上沙箱 VM 将 Three.js 编译为 Android/iOS/visionOS/WebXR 原生渲染
- three-live-cli 提供 MCP 服务器与 agent gym（validate/render/convert/from-image 等工具）
- Web 组件支持任意 Chat Completions 兼容后端驱动场景编辑与语音交互
- 图像/蓝图转场景并经空间质量门校验与闭环视觉精修

## 适用场景

- 让 AI 代理生成并通过接触表验证 Three.js 场景再编译到移动端
- 在 Web 页面中让用户用语音或文字由 LLM 修改 3D 场景
- 把照片或蓝图转成可运行的程序化 Three.js 场景

## 场景标签

`代码生成` `多模态` · 领域:编码与开发

## 证据(README 行号)

> L5: **AI-First Native 3D, CAD & Spatial Computing:** On-device JIT compiler turning live, AI-generated **Three.js** into
> L63: `three-live-cli mcp` as a zero-dependency **Model Context Protocol (MCP)** stdio
> L112: `ai-endpoint` speaks the widely supported Chat Completions protocol

## 星数曲线

```mermaid
xychart-beta
    title "google/three-live 星数(近 16 点)"
    x-axis ["2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 183 --> 546
    line [213, 322, 338, 374, 390, 403, 422, 432, 446, 462, 466, 475, 478, 495, 509, 516]
```

2026-11-08 213 → 2026-11-27 516（+303）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `830e0410fafc` · [字段定义](../../DATASET.md)*
