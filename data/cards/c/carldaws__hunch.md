# carldaws/hunch

⭐ 20 · Ruby · MIT · 推送 2026-09-25 · [GitHub](https://github.com/carldaws/hunch) · 个人维护

**Ruby/Rails 概率决策库：用自然语言提问获取校准概率**

Ruby gem，为 Ruby 与 Rails 应用提供概率式控制流：以英文问句描述判断（如订单是否欺诈、邮件是否垃圾），通过 System One 后端（如 TypeSafe 的 Jev）返回校准概率而非文本，并以 Ruby 值交付。提供 chance/pick/rate 三类原语、可配置阈值谓词、Hunch.decide 批量提问、Rails 校验与邮件路由等示例，以及测试用 Stub 后端；后端为任意实现 decide 协议的对象，需配置 System One 端点（Jev 经 OpenRouter 提供）。另有 TypeScript 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- chance/pick/rate 三类概率决策原语，答案以 Ruby 值返回
- Hunch.decide 在一次 API 调用中批量提问
- 测试用 Stub 后端，无需 API 调用即可断言
- 后端可替换：任意实现 decide(state:, questions:) 协议的对象

## 适用场景

- 在 Rails 校验中拦截垃圾注册信息
- 按邮件内容自动路由到对应团队
- 根据错误信息与重试次数决定任务是否重试
- 将导入文本映射到已有枚举值

## 场景标签

 · 领域:LLM 应用库/Ruby 开发

## 证据(README 行号)

> L17: Hunch asks a System One model, such as TypeSafe's Jev,
> L218: `Hunch::Backends::SystemOne` talks to any endpoint that speaks the System One

## 星数曲线

```mermaid
xychart-beta
    title "carldaws/hunch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-31 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `394bf661db34` · [字段定义](../../DATASET.md)*
