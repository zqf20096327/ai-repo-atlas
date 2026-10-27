# ModelJars/modeljars

⭐ 26 · Java · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/ModelJars/modeljars) · [官网](https://modeljars.org) · 组织维护

**JVM 生态的模型编目与分发规范：用 Maven 坐标管理本地模型**

社区维护的 marker-JAR 约定与目录：为本地/远程模型工件赋予普通 JVM 依赖坐标与 classpath 元数据，大权重文件保留在外部（指向 Hugging Face 等上游的 commit 固定版本与 SHA-256），紧凑负载可打包进 JAR。每个 marker 携带许可、量化变体、后端兼容性与性能档案等元数据，Gradle 生成聚合目录。配套 GraalVM 原生 CLI（无需 JDK）支持搜索、校验下载、缓存管理、硬件可运行性检查与 JBang demo 生成；JVM Runtime 需 Java 25+，可选 CUDA/Tornado 后端做 GPU 加速。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- marker JAR 携带许可、量化变体、后端兼容性、性能档案等机器可读元数据
- pull 按 SHA-256 与字节大小逐文件校验，内容寻址缓存，不启动推理
- CLI 为 GraalVM 原生可执行文件，无需 JDK；支持 JSON/plain 输出与别名
- 模型检查点（catalog/models.json）与性能证据独立版本化管理，含发布资格审查

## 适用场景

- 在 Maven/Gradle 工程中以依赖坐标声明并加载模型
- 下载前审查模型来源、许可与本地硬件可运行性
- 为聊天/嵌入/语音/重排等能力生成可运行的 JBang 示例程序

## 场景标签

 · 领域:LLM 基础设施/模型分发

## 证据(README 行号)

> L5: ModelJars is a community-owned marker-JAR convention for local and remote model artifacts.
> L47: The `modeljars` CLI is a self-contained GraalVM native executable; using it does not require a JDK.
> L147: Applications use the stable JVM Runtime artifact and add one model dependency for every model they

## 星数曲线

```mermaid
xychart-beta
    title "ModelJars/modeljars 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `91985756a30a` · [字段定义](../../DATASET.md)*
