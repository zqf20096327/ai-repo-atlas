# sderosiaux/chrome-agent

⭐ 96 · Rust · MIT · 推送 2026-10-12 · [GitHub](https://github.com/sderosiaux/chrome-agent) · 个人维护 · 中文 README

**供 AI agent 驱动 Chrome 的 Rust CLI：执行操作并回报页面真实结果**

单一约 3 MB 的 Rust 二进制，通过 Chrome DevTools Protocol 驱动浏览器，面向调用方 AI agent 提供 CLI 与 JSON stdin/stdout 管道。提供导航、无障碍树读取（稳定 uid）、点击/填表等操作、断言、网络与控制台监控、宏录制与持久化发现协议。每个变更操作附带 verdict/verdict_reason/next 判定（changed/intercepted/not_kept 等），报告拦截点击与缺失观察，供调用 agent 校验实际效果。自主发现与公共配方目录尚在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 变更操作返回 closed-set verdict/next，报告页面是否真正服从
- 无障碍树稳定 uid，一次 inspect 多次操作
- 3 MB Rust 单二进制，无 Node、无云依赖，Linux 为静态 musl 构建
- 支持 batch/pipe 持久 JSON 连接、宏录制与跨进程实验记录

## 适用场景

- 让编码 agent 在浏览器中执行并验证网页任务
- 从页面提取结构化数据（自动识别重复记录、Readability 正文）
- 对表单填写与点击结果做断言校验
- 并行运行多个命名浏览器会话供多个 agent 使用

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L16: maintain themselves. The calling agent supplies the reasoning; chrome-agent preserves the
> L21: Today, chrome-agent provides the execution foundation: a 3 MB Rust binary over CDP, browser
> L156: `ok:true` means the command ran, not that the page complied. Every mutating action carries a

## 星数曲线

```mermaid
xychart-beta
    title "sderosiaux/chrome-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 94 --> 97
    line [95, 96, 96]
```

2026-10-18 95 → 2026-10-24 96（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `92d2c3b60eab` · [字段定义](../../DATASET.md)*
