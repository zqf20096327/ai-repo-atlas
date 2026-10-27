# mondaycom/HATCHA

⭐ 104 · TypeScript · MIT · 推送 2026-03-11 · [GitHub](https://github.com/mondaycom/HATCHA) · [官网](https://usehatcha.dev) · 组织维护

**反向验证码组件：只放行 AI agent，拦截人类访问**

monday.com 开源的反向 CAPTCHA：通过大数乘法、字符串反转、二进制解码等对 AI 轻松、对人类困难的题目来验证访问者是 agent。服务端 HMAC 签名令牌做无状态校验，答案不下发客户端，无需数据库。内置 5 种挑战类型，支持运行时注册自定义挑战生成器，提供 Next.js App Router 与 Express 适配器及 React 组件，主题可通过 CSS 自定义属性切换。

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

- 服务端 HMAC 签名令牌的无状态验证，无需数据库
- 5 种内置挑战类型（大数乘法/字符串反转/计数/排序/二进制解码）
- 运行时注册自定义挑战生成器
- Next.js 与 Express 框架适配器开箱可用

## 适用场景

- 为 AI agent 专属入口做访问验证，拦下人类用户
- 在 Next.js/Express 应用中集成 agent 门禁
- 按业务需要扩展自定义挑战类型

## 场景标签

 · 领域:Web 开发/AI agent 基础设施

## 证据(README 行号)

> L2:  CAPTCHA proves you're human. HATCHA proves you're not.
> L10: HATCHA (**H**yperfast **A**gent **T**est for **C**omputational **H**euristic **A**ssessment) is a reverse CAPTCHA t

## 星数曲线

```mermaid
xychart-beta
    title "mondaycom/HATCHA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-27 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `37a0516dae96` · [字段定义](../../DATASET.md)*
