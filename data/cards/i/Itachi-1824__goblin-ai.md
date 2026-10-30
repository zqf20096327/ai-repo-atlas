# Itachi-1824/goblin-ai

⭐ 20 · JavaScript · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/Itachi-1824/goblin-ai) · 个人维护

**免注册免费 AI 生图 Python 库，支持 30+ 模型与本地 UI**

提供 Python API、CLI、本地 Web UI 与 HTTP API 生成 AI 图像，覆盖 Flux、SDXL、动漫、写实等 30+ 模型，普通使用无需账号或个人 API key，首次使用执行建立托管会话，后续复用。附 PNG 增强、多档放大（插值与 SPAN/MoSR/RealPLKSR/DAT2 神经模型，需 cpu/gpu extra），默认输出 768×768 PNG。生成依赖上游服务，可用性受其影响；分发为平台编译 wheel 无源码，采用专有许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python/CLI/UI/HTTP API 多入口生图，30+ 模型含 Flux、SDXL、动漫、写实
- 普通使用无需账号或 API key，托管会话复用
- 多档放大预设：插值 fast 及 SPAN/MoSR/RealPLKSR/DAT2 神经模型
- 服务器默认绑定 localhost，带 /health 与请求限流，公开暴露需认证反代

## 适用场景

- 在 Python 脚本或批处理中生成 AI 图像
- 本地浏览器 UI 中按提示词自动路由模型生图
- 对生成图像做神经放大与 PNG 增强

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L3: ### Image generation from Python or a local browser interface
> L14: Generate AI images from Python or a local browser interface, with optional CPU/GPU upscaling. No account or persona

## 星数曲线

```mermaid
xychart-beta
    title "Itachi-1824/goblin-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ad4a1e43ce0d` · [字段定义](../../DATASET.md)*
