# xsignon-secure/AutoHeal-AI

⭐ 4 · TypeScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/xsignon-secure/AutoHeal-AI) · 组织维护

**自托管 AI agent：修复 CI 中失败的 Playwright 等测试**

以 npm 包形式提供的自托管 agent：读取 GitHub Actions、GitLab CI、CircleCI 或本机的测试失败报告，判定失败原因（测试缺陷、应用缺陷、flaky、截图基线、环境问题），修复测试并连续重跑证明稳定后以 draft PR 提交证据。通过代码扫描与运行时守卫阻止削弱断言等作弊改动，MIT 许可，不依赖其服务器、无账号与遥测，AI 调用使用用户自己的 key，并可完全不用 AI（基于元素指纹的规则修复）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 失败分类处理：测试缺陷出 PR、应用缺陷出 issue、flaky 加隔离与过期机制
- 反作弊双层防护：代码扫描（token 级白名单）+ 运行时 trace 对比
- 元素指纹记录定位器指向，改名按钮可无 AI token 修复
- Linux runner 上以独立用户沙箱运行测试与修复，隔离 AI key

## 适用场景

- CI 中 Playwright 测试因 UI 改动失败后自动出修复 PR
- 识别并隔离 flaky 测试，附责任人与过期日期
- 截图基线在应用代码变更后自动重录并证明
- 团队通过 .autoheal.yml 策略限制 agent 可修改范围

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **A free, self-hosted AI agent that fixes failing Playwright, pytest, Cypress and WebdriverIO tests in GitHub Action
> L13: When your Playwright (or pytest, Cypress or WebdriverIO) workflow fails, AutoHeal reads the report and traces, deci

## 星数曲线

```mermaid
xychart-beta
    title "xsignon-secure/AutoHeal-AI 星数(近 3 点)"
    x-axis ["2026-11-14", "2026-11-19", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-14 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 low · 依据 README sha `0808a876f24d` · [字段定义](../../DATASET.md)*
