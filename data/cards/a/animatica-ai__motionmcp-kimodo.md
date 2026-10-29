# animatica-ai/motionmcp-kimodo

⭐ 23 · Python · Apache-2.0 · 推送 2026-05-27 · [GitHub](https://github.com/animatica-ai/motionmcp-kimodo) · 组织维护

**把 NVIDIA Kimodo 动作生成模型封装为自托管 MMCP 服务器**

实现 motionmcp.Backbone 接口的参考服务端：加载 Kimodo（SOMA）动作扩散模型权重，将 MMCP 请求映射为推理调用，经 /generate 端点以 glTF 返回动画，支持根路径、末端效应器目标与姿态关键帧约束。面向熟悉 Python、CUDA 与自托管 ML 服务的开发者，通过 pip 从 git 安装，首次安装需编译 MotionCorrection（CMake + C++），可耗时 30 分钟以上。参考客户端为 Proscenium for Blender，也可将 KimodoBackbone 嵌入 FastAPI/ASGI 应用。项目处于 Alpha，API 与打包可能变化；艺术家可改用 animatica.ai 托管服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 实现 MMCP Backbone：/generate 端点返回 glTF 动画
- 支持根路径、末端效应器目标、姿态关键帧约束
- CLI 一条命令启动（motionmcp-kimodo --port 8000），可 LAN 使用
- KimodoBackbone 可嵌入自定义 FastAPI/ASGI 应用

## 适用场景

- 在自有 GPU 上运行 Kimodo 并通过 HTTP 对外提供动作生成
- 配合 Proscenium 插件在 Blender 中按文本提示与骨骼约束生成动画
- 把 Kimodo 推理能力嵌入自己的 ASGI 服务

## 场景标签

 · 领域:角色动画/生成式 AI 基础设施

## 证据(README 行号)

> L7: **Self-hosted MMCP server for Kimodo motion generation.**
> L21: - **MMCP-native** — implements `motionmcp.Backbone`; capabilities, `/generate`, glTF responses
> L22: - **Kimodo SOMA models** — loads Kimodo checkpoints; maps MMCP requests to Kimodo inference

## 星数曲线

```mermaid
xychart-beta
    title "animatica-ai/motionmcp-kimodo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 24
    line [22, 23]
```

2026-10-18 22 → 2026-10-29 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `0a5bf1a31a78` · [字段定义](../../DATASET.md)*
