# takahirom/arbigent

⭐ 651 · Kotlin · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/takahirom/arbigent) · 个人维护

**面向 Android/iOS/Web/TV 的 AI Agent 自动化测试框架**

Arbigent 是一个用 AI agent 驱动的应用测试框架：将复杂目标拆解为相互依赖的场景（如登录→搜索）并编排执行，支持 iOS、Android、Web 和 D-pad 导航的 TV 界面。QA 工程师可在 UI 中以自然语言定义目标，工程师可用 YAML 文件以代码方式执行并接入既有测试设施。默认使用 gpt-4.1，也支持 gpt-4o-mini 等模型；通过 UI 树优化、带标注截图、图像断言复检、卡屏检测提升可靠性。另支持 MCP 外部工具、Maestro YAML 流程复用与 AI 结果缓存/重放降本。需连接真机或模拟器并输入 AI 提供商 API key。作者自评速度（1/5）与资源成本（GPT-4o 下约每步 $0.005）为当前限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 场景拆解与依赖编排（login -> search 等互联场景）
- UI 可视化建场景 + YAML 代码执行的混合工作流
- 支持 iOS/Android/Web/TV（含 D-pad 导航）测试
- MCP 外部工具接入与 Maestro YAML 流程复用

## 适用场景

- 让 QA 工程师用自然语言描述目标自动测试移动/Web 应用
- 把复杂测试目标拆成多个依赖场景做规模化 AI 测试
- 复用已有 Maestro 测试脚本作为 AI 测试前的初始化步骤
- 通过 MCP 服务器在测试中调用安装应用、查日志等外部工具

## 场景标签

`GUI 自动化` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L23: To address these challenges, I created Arbigent, an AI agent testing framework that can break down complex tasks in
> L45:  * **Orchestration:** Acts as a mediator, managing the execution flow of AI agents across multiple, interconnected 

## 星数曲线

```mermaid
xychart-beta
    title "takahirom/arbigent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 650 --> 653
    line [651, 652, 651]
```

2026-10-18 651 → 2026-10-25 651（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `b6d36901c5d4` · [字段定义](../../DATASET.md)*
