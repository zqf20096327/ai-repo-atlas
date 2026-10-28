# DecartAI/decart-python

⭐ 21 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/DecartAI/decart-python) · [官网](https://docs.platform.decart.ai/sdks/python) · 组织维护

**Decart AI 平台的 Python SDK：接入图像/视频编辑与实时模型**

由 DecartAI 维护的异步 Python SDK，用于调用 Decart 平台模型：Process API 做图像编辑，Queue API 提交并轮询视频编辑任务，Realtime API 建立实时会话（支持 speed='fast' 高算力档，限特定 lucy 系列模型与美国区域）。另支持签发短期客户端 JWT token，并以 PyJWT+cryptography 做 Ed25519/JWKS 离线验签。SDK 为 async-only，提供 uv/pip 安装及 Gradio 测试 UI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Process/Queue API 覆盖图像与视频编辑任务
- 实时会话 fast 模式（限 lucy 系列模型、美国区域、2x 计费）
- 客户端 JWT token 签发与 Ed25519/JWKS 离线验签（decart[verify] 扩展）
- async-only 设计，附 Gradio 交互式测试 UI

## 适用场景

- 在 Python 应用中调用 Decart 平台的图像/视频编辑能力
- 前后端架构下签发短期 token 并在本地离线验签
- 不写代码即可通过测试 UI 试用 SDK 各功能

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: A Python SDK for Decart's models.
> L40: async with DecartClient(api_key=os.getenv("DECART_API_KEY")) as client:

## 星数曲线

```mermaid
xychart-beta
    title "DecartAI/decart-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1c9df84f12be` · [字段定义](../../DATASET.md)*
