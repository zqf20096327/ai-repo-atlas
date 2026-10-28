# christian-bromann/ZeitZeuge

⭐ 25 · TypeScript · NOASSERTION · 推送 2026-03-13 · [GitHub](https://github.com/christian-bromann/ZeitZeuge) · [官网](https://zeitzeuge.dev) · 个人维护

**前端加载与 Vitest 测试的性能分析工具：AI 代理定位瓶颈**

面向前端与测试开发者的性能诊断工具：CLI 模式经 WebdriverIO 启动 Chrome，采集 V8 堆快照、性能 trace、运行时 trace 与网络资源；Vitest 插件模式注入 --cpu-prof 采集每文件 CPU profile。采集数据写入内存虚拟文件系统，由 LangChain Deep Agent 自主浏览源码并交叉分析，输出 Markdown 报告与代码级修复建议。LLM 支持 OpenAI 与 Anthropic（按环境变量自动检测），需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 页面加载模式下采集 V8 堆快照、性能 trace、Chrome 运行时 trace 与网络资源
- Vitest 插件注入 --cpu-prof 并按 application/dependency/test/framework 分类热点函数
- Deep Agent 在内存 VFS 中读取源码，输出含代码级修复的 Markdown 报告
- 检测内存泄漏、帧阻塞函数、事件监听器泄漏、GC 压力等问题

## 适用场景

- 分析页面加载慢的根因并获取修复建议
- 找出 Vitest 测试变慢时应用代码中的热点函数
- 排查内存泄漏与事件监听器泄漏

## 场景标签

 · 领域:前端/测试工程与性能分析

## 证据(README 行号)

> L5: AI-powered performance analysis for frontend page loads and Vitest test suites. Captures V8 heap snapshots, performa
> L65: 4. **Deep Agent explores** — a LangChain Deep Agent (`deepagents`) autonomously browses the workspace, reads actual

## 星数曲线

```mermaid
xychart-beta
    title "christian-bromann/ZeitZeuge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5b703a3063b6` · [字段定义](../../DATASET.md)*
