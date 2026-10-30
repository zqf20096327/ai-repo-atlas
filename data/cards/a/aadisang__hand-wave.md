# aadisang/hand-wave

⭐ 21 · Swift · MIT · 推送 2026-10-08 · [GitHub](https://github.com/aadisang/hand-wave) · [官网](https://handwave.sh) · 个人维护

**基于智能眼镜与美国手语手指拼写的手势识别转语音应用**

面向 Web 与 iOS 的手语手指拼写识别应用，前端为 Expo 移动应用与网站，后端由一个小型 Python 推理服务（通过 Modal 部署）提供神经网络推理，将识别结果转为语音。工具链使用 pnpm、Node 22、Python 3.11/3.12、uv、moon 与 Git LFS；开发模式一键启动隔离的 Modal 后端并配置双端客户端。README 提及 YouTube 演示视频并列出多项手势识别研究作为来源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Web 与 iOS 双客户端（Expo 移动应用）
- 小型 Python 推理服务经 Modal 部署
- pnpm test 提供真实服务检查与 e2e 证据留档
- 合并到 main 自动发布 TestFlight 与网站

## 适用场景

- 佩戴智能眼镜将 ASL 手指拼写实时转为语音
- 在浏览器或 iPhone 上体验手语识别演示
- 作为手势识别研究的工程化参考实现

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L1: # Hand Wave
> L3: Sign recognition for web and iOS, backed by a small Python inference service.
> L5: Watch the demo on YouTube

## 星数曲线

```mermaid
xychart-beta
    title "aadisang/hand-wave 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `96bab2e3c507` · [字段定义](../../DATASET.md)*
