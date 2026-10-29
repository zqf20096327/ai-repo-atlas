# microsoft/typechat.net

⭐ 230 · C# · MIT · 推送 2026-10-27 · [GitHub](https://github.com/microsoft/typechat.net) · 组织维护

**.NET 库：用强类型 schema 把自然语言意图翻译为 JSON 对象与程序**

微软维护的 TypeChat 思想在 .NET 上的实现，面向用 C# 构建自然语言接口的开发者。提供三个程序集：JsonTranslator 把用户意图翻译为符合 TypeScript 表达 schema 的强类型对象，含验证、修复与反序列化；Program 模块把意图合成为带文法约束的 JSON 程序（Plan），可解释执行或经 DLR 编译；SemanticKernel 集成模块。当前需 OpenAI 模型访问（支持 Azure OpenAI），也可通过实现 ILanguageModel 接入自有客户端。README 声明处于活跃开发、API 会演进，仅测试过 TypeScript schema。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 意图→符合 schema 的强类型 JSON，含验证失败回送模型自动修复
- JSON 程序（Plan）：文法约束、类型检查、解释器或 DLR 编译执行
- Vocabulary 词表属性约束字符串取值，支持运行时动态加载
- Semantic Kernel 集成：模型、插件与嵌入访问

## 适用场景

- 把自然语言点单/日历/订餐请求转为可执行的业务对象
- 将用户意图编译为调用插件 API 的类型安全程序
- 构建带交互历史的强类型消息型 agent

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: TypeChat.NET provides **cross platform** libraries that help you build natural language interfaces with language mod
> L29: TypeChat uses language models to translate user intent into JSON that conforms to a schema. This JSON is then valid

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/typechat.net 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 229 --> 231
    line [230, 230]
```

2026-10-18 230 → 2026-10-29 230（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8d8ce3d56ede` · [字段定义](../../DATASET.md)*
